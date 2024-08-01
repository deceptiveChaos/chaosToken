# -*- coding: utf-8 -*-
import paramiko
import pathlib

__all__ = [
    'create_local_file',
    'send_file_over_ssh',
    'create_and_send_file'
]

"""def create_local_file(file_path: str, file_content: str) -> str:
    file_dir = pathlib.Path(file_path).parent
    if not file_dir.exists():
        file_dir.mkdir(parents=True)
    with open(file_path, 'w') as f:
        f.write(file_content)
    return file_path"""

def create_local_file(folder_path: pathlib.Path) -> list:
    files = []
    for file in folder_path.iterdir():
        files.append(file)
    return files

def send_file_over_ssh(
    file_path: str, 
    host: str, 
    username: str, 
    password: str
) -> None:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(
            hostname=host, 
            username=username, 
            password=password
        )
        sftp = ssh.open_sftp()
        sftp.put(file_path, file_path)
    finally:
        ssh.close()

def create_and_send_file(
    file_path: str, 
    file_content: str, 
    host: str, 
    username: str, 
    password: str
) -> str:
    file_path = create_local_file(file_path, file_content)
    
    send_file_over_ssh(
        file_path, 
        host, 
        username, 
        password
    )
    return file_path