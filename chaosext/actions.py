# -*- coding: utf-8 -*-
import paramiko
import pathlib
import random

__all__ = [
    'create_local_files',
    'send_file_over_ssh',
    'send_files_to_host',
    'send_files_to_hosts'
]

def create_local_files(folder_path: str) -> list:
    folder_path = pathlib.Path(folder_path)
    files = []
    for file in folder_path.iterdir():
        files.append(file)
    return files

def send_file_over_ssh(
    file_path: str, 
    host: str, 
    username: str, 
    password: str, 
    remote_subfolder: str
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
        file_path = pathlib.Path(file_path)
        remote_file_path = str(pathlib.Path(remote_subfolder) / file_path.name)
        sftp.put(str(file_path), remote_file_path)
    finally:
        ssh.close()

def send_files_to_host(
    folder_path: str, 
    host: str, 
    username: str, 
    password: str, 
    remote_folder: str,
    remote_subfolders: list
) -> None:
    folder_path = pathlib.Path(folder_path)
    remote_folder = pathlib.Path(remote_folder)
    files = create_local_files(folder_path)

    for file in files:
        remote_subfolder_name = random.choice(remote_subfolders)
        remote_subfolder = remote_folder / remote_subfolder_name
        send_file_over_ssh(
            str(file), 
            host, 
            username, 
            password, 
            str(remote_subfolder)
        )

def send_files_to_hosts(
    folder_path: str, 
    hosts: list, 
    remote_folder: str,
    remote_subfolders: list
) -> None:
    folder_path = pathlib.Path(folder_path)
    remote_folder = pathlib.Path(remote_folder)
    files = create_local_files(folder_path)

    for host in hosts:
        host_ip = host['host']
        username = host['username']
        password = host['password']

        for file in files:
            remote_subfolder_name = random.choice(remote_subfolders)
            remote_subfolder = remote_folder / remote_subfolder_name
            send_file_over_ssh(
                str(file), 
                host_ip, 
                username, 
                password, 
                str(remote_subfolder)
            )