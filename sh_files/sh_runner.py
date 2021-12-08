import subprocess


def queue_set():
    user_id = int(subprocess.check_output(["sh", "./sh_files/are_u_root.sh"]).decode("utf-8"))
    if user_id:
        print("Go to root mode!")
    else:
        subprocess.run(["sh", "./sh_files/queue_set.sh"])
    return user_id


def proxy_off():
    subprocess.run(["sh", "./sh_files/proxy_off.sh"])
