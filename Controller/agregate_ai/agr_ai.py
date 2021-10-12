from keras.applications.densenet import layers
from tensorflow import keras
import tensorflow as tf



(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Предобработаем данные (это массивы Numpy)
x_train = x_train.reshape(60000, 784).astype('float32') / 255
x_test = x_test.reshape(10000, 784).astype('float32') / 255

y_train = y_train.astype('float32')
y_test = y_test.astype('float32')

# Зарезервируем 10,000 примеров для валидации
x_val = x_train[-10000:]
y_val = y_train[-10000:]
x_train = x_train[:-10000]
y_train = y_train[:-10000]

# Получим модель
inputs = keras.Input(shape=(784,), name='digits')
x = layers.Dense(64, activation='relu', name='dense_1')(inputs)
x = layers.Dense(64, activation='relu', name='dense_2')(x)
outputs = layers.Dense(10, activation='softmax', name='predictions')(x)
model = keras.Model(inputs=inputs, outputs=outputs)

# Создадим экземпляр оптимизатора для обучения модели.
optimizer = keras.optimizers.SGD(learning_rate=1e-3)
# Создадим экземпляр функции потерь.
loss_fn = keras.losses.SparseCategoricalCrossentropy()

# Подготовим метрику.
train_acc_metric = keras.metrics.SparseCategoricalAccuracy()
val_acc_metric = keras.metrics.SparseCategoricalAccuracy()

# Подготовим тренировочный датасет.
batch_size = 64
train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
train_dataset = train_dataset.shuffle(buffer_size=1024).batch(batch_size)

# Подготовим валидационный датасет.
val_dataset = tf.data.Dataset.from_tensor_slices((x_val, y_val))
val_dataset = val_dataset.batch(64)

# Итерируем по эпохам.
epochs = 3
for epoch in range(epochs):
    print('Начало эпохи %d' % (epoch,))

    # Итерируем по пакетам в датасете.
    for step, (x_batch_train, y_batch_train) in enumerate(train_dataset):
        with tf.GradientTape() as tape:
            logits = model(x_batch_train)
            loss_value = loss_fn(y_batch_train, logits)
        grads = tape.gradient(loss_value, model.trainable_weights)
        optimizer.apply_gradients(zip(grads, model.trainable_weights))

        # Обновляем метрику на обучении.
        train_acc_metric(y_batch_train, logits)

        # Пишем лог каждые 200 пакетов.
        if step % 200 == 0:
            print('Потери на обучении (за один пакет) на шаге %s: %s' % (step, float(loss_value)))
            print('Уже просмотрено: %s примеров' % ((step + 1) * 64))

    # Покажем метрики в конце каждой эпохи.
    train_acc = train_acc_metric.result()
    print('Accuracy на обучении за эпоху: %s' % (float(train_acc),))
    # Сбросим тренировочные метрики в конце каждой эпохи
    train_acc_metric.reset_states()

    # Запустим валидационный цикл в конце эпохи.
    for x_batch_val, y_batch_val in val_dataset:
        val_logits = model(x_batch_val)
        # Обновим валидационные метрики
        val_acc_metric(y_batch_val, val_logits)
    val_acc = val_acc_metric.result()
    val_acc_metric.reset_states()
    print('Accuracy на валидации: %s' % (float(val_acc),))
