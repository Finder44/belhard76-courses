import yaml


def read_yaml_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)


def get_task_dependencies(task_name, task_dict, all_tasks, visited):
    if task_name in visited:
        return
    visited.add(task_name)
    dependencies = task_dict.get(task_name, [])
    for dep in dependencies:
        get_task_dependencies(dep, task_dict, all_tasks, visited)
    all_tasks.append(task_name)


def get_tasks_for_build(build_name, builds_data, tasks_data):
    build = next((build for build in builds_data['builds'] if build['name'] == build_name), None)
    if not build:
        return []

    task_dict = {task['name']: task['dependencies'] for task in tasks_data['tasks']}
    all_tasks = []
    visited = set()

    for task in build['tasks']:
        get_task_dependencies(task, task_dict, all_tasks, visited)

    return all_tasks


# Чтение данных из YAML файлов
builds_data = read_yaml_file('builds.yaml')
tasks_data = read_yaml_file('tasks.yaml')

# Получение задач для конкретного билда
build_name = 'forward_interest'
task_list = get_tasks_for_build(build_name, builds_data, tasks_data)

# Вывод результата
print(f"Билд - {build_name}")
print("Список задач:")
for task in task_list:
    print(task)

print(f"\nПримечание: Для {build_name} список должен получиться длиной {len(task_list)}")
