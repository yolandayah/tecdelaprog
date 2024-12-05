#!/usr/bin/env python3
#
# Yolanda Alejo Huarta
#

import asyncio
from multiprocessing import Process, Queue
import time
import os


async def perform_task(task):
    await asyncio.sleep(task)  # Simula una larga tarea
    return task ** 2


async def worker_main(worker_id, task_queue, result_queue):
    print(f"Worker {worker_id} comenzando (PID: {os.getpid()})")
    while True:
        task = task_queue.get()  # Se bloquea hasta que una tarea este disponible
        if task is None:  # Apaga la señal
            print(f"Worker {worker_id} apagando.")
            break
        try:
            result = await perform_task(task)
            result_queue.put((worker_id, task, result))
        except Exception as e:
            print(f"Worker {worker_id} encontró un error: {e}")

# Proceso de los workers
def worker_process(worker_id, task_queue, result_queue):
    asyncio.run(worker_main(worker_id, task_queue, result_queue))


def master_main(task_queue, result_queue, num_workers):
    # Comenzando los procesos de los workers
    workers = []
    for i in range(num_workers):
        worker = Process(target=worker_process, args=(i, task_queue, result_queue))
        workers.append(worker)
        worker.start()
    
    # Mandar las tareas
    tasks = [1, 2, 3, 4, 5]  # Tareas de ejemplo
    for task in tasks:
        task_queue.put(task)

    # Obteniendo resultados
    print("Master obteniendo resutlados:")
    for _ in tasks:
        worker_id, task, result = result_queue.get()
        print(f"Worker {worker_id} procesando tarea {task}: resultado {result}")

    # Señal para los workers para que se apaguen
    for _ in range(num_workers):
        task_queue.put(None)

    # Esperar a los workers que terminen
    for worker in workers:
        worker.join()

    print("Todos los workers se han apagado.")


task_queue = Queue()
result_queue = Queue()

if __name__ == "__main__":
    num_workers = 4
    master_main(task_queue, result_queue, num_workers)

