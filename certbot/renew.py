import os
import sys
import subprocess
from datetime import datetime


def now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def log(msg):
    print(f"[ {now()} ] {msg}")


def log_err(msg):
    print(f"[ {now()} ] ERROR: {msg}", file=sys.stderr)


def main():
    log("=== Certificate renewal process started ===")

    certbot_dir = os.path.expanduser("/home/very_lazy/lzy.su/certbot")
    try:
        os.chdir(certbot_dir)
    except OSError as e:
        log_err(f"Failed to switch to certbot directory! {e}")
        log("Error occurred. See error log.")
        sys.exit(1)

    log("Running certbot renew (nginx will reload only if certificate is renewed)...")

    deploy_hook = (
        f"echo '[ {now()} ] Deploy hook: reloading nginx...' && "
        f"cd {os.path.expanduser('~')}/lzy.su && "
        "docker compose exec lzysu-nginx-prod nginx -s reload && "
        f"echo '[ {now()} ] Deploy hook: nginx reload completed.'"
    )

    cmd = [
        "docker", "compose", "run", "--rm", "certbot", "renew",
        "--webroot", "-w", "/etc/letsencrypt", "--quiet",
        "--deploy-hook", deploy_hook
    ]
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    if proc.returncode != 0:
        log_err("Certificate renewal failed! Certbot output:")
        log("Error occurred. See error log.")
        print(proc.stdout, file=sys.stderr)
        sys.exit(2)
    else:
        log("Certificate renewal process finished. If certificate was renewed, nginx was reloaded.")

    log("=== Certificate renewal process finished ===")


if __name__ == "__main__":
    main()
