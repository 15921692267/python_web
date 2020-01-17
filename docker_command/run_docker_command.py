#!/usr/bin/python3
#_*_ coding: utf-8 _*_

import os

def view_docker_images():
    print()
    print("\033[32;1mInfo: 查看已有的镜像\033[0m")
    os.system("docker images")

def view_run_container_info():
    print()
    print("\033[32;1mInfo: 查看正在运行的容器\033[0m")
    os.system("docker ps")

def view_all_of_container_info():
    print()
    print("\033[32;1mInfo: 查看所有的容器\033[0m")
    os.system("docker ps -a")

def create_docker_container(image_id, src_port, des_port, names):
    os.system("docker run -d -p {des_port}:{src_port} --name {names} {image_id}".format(
        des_port=des_port,
        src_port=src_port,
        names=names,
        image_id=image_id
    ))
    print("The container creates success")

def stop_container(container_id):
    os.system("docker stop {container_id}".format(container_id=container_id))
    print("\033[32;1mInfo:\033[0m The containner {container_id} already stop".format(container_id=container_id))

def start_container(container_id):
    os.system("docker start {container_id}".format(container_id=container_id))
    print("\033[32;1mInfo:\033[0m The containner {container_id} already start".format(container_id=container_id))

def delete_container(container_id):
    os.system("docker rm {container_id}".format(container_id=container_id))
    print("\033[32;1mInfo:\033[0m The containner {container_id} already deleted".format(container_id=container_id))

def delete_all_of_container():
    container_List = os.popen("docker ps -a -q")
    for line in container_List:
        # print(line)
        os.system("docker rm %s" % line)
    print("\033[32;1mInfo:\033[0m All of container already deleted")

def restart_docker_service():
    os.system("systemctl restart docker")

view_docker_images()
view_all_of_container_info()
view_run_container_info()
while True:
    print()
    msg_info = """
    0.quit 
    1.create container  
    2.stop container 
    3.start container 
    4.view running container 
    5.view all of container
    6.view docker images
    7.delete container 
    8.delete all of container
    9.restart docker service
    """
    print(msg_info)
    input_number = input("\033[34;1mPlease chioce number:\033[0m ")
    if input_number == "0".strip():
        print("Programs quit")
        break
    if input_number == "1".strip():
        image_id = input("\033[34;1mPlease input docker image id:\033[0m ")
        src_port = input("\033[34;1mPlease input source port:\033[0m ")
        des_port = input("\033[34;1mPlease input map port:\033[0m ")
        container_name = input("\033[34;1mPlease input container name:\033[0m ")
        create_docker_container(image_id, src_port, des_port, container_name)
    if input_number == "2".strip():
        container_id = input("\033[34;1mPlease input docker container id:\033[0m ")
        stop_container(container_id)
    if input_number == "3".strip():
        container_id = input("\033[34;1mPlease input docker container id:\033[0m ")
        start_container(container_id)
    if input_number == "4".strip():
        view_run_container_info()
    if input_number == "5".strip():
        view_all_of_container_info()
    if input_number == "6".strip():
        view_docker_images()
    if input_number == "7".strip():
        # running container can not delete
        container_id = input("\033[34;1mPlease input docker container id:\033[0m ")
        delete_container(container_id)
    if input_number == "8".strip():
        delete_all_of_container()
    if input_number == "9".strip():
        restart_docker_service()



