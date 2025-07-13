from project import Project
from datetime import datetime

FILENAME = "projects.txt"


def load_projects(filename):
    projects = []
    with open(filename, "r") as file:
        next(file)  # Skip header
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 5:
                name, start_date, priority, cost, completion = parts
                projects.append(Project(name, start_date, int(priority), float(cost), int(completion)))
    return projects


def save_projects(filename, projects):
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for p in projects:
            file.write(f"{p.name}\t{p.start_date.strftime('%d/%m/%Y')}\t{p.priority}\t{p.cost_estimate}\t{p.completion_percentage}\n")


def display_projects(projects):
    incomplete = []
    complete = []

    for project in projects:
        if project.is_complete():
            complete.append(project)
        else:
            incomplete.append(project)

    incomplete.sort()
    complete.sort()
    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects:")
    for p in complete:
        print(f"  {p}")


def filter_projects_by_date(projects, date_str):
    date = datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered_projects = []
    for p in projects:
        if p.start_date > date:
            filtered_projects.append(p)
    filtered_projects.sort(key=lambda x: x.start_date)
    for p in filtered_projects:
        print(p)


def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost, completion))


def update_project(projects):
    for i, p in enumerate(projects):
        print(f"{i} {p}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    new_completion = input("New Percentage: ")
    if new_completion != "":
        project.completion_percentage = int(new_completion)
    new_priority = input("New Priority: ")
    if new_priority != "":
        project.priority = int(new_priority)

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    run_menu(projects)


def run_menu(projects):
    print("- (L)oad projects\n"
          "- (S)ave projects\n"
          "- (D)isplay projects\n"
          "- (F)ilter projects by date\n"
          "- (A)dd new project\n"
          "- (U)pdate project\n"
          "- (Q)uit")

    choice = input(">>> ").strip().lower()

    if choice == "l":
        filename = input("Filename: ")
        projects = load_projects(filename)
    elif choice == "s":
        filename = input("Filename: ")
        save_projects(filename, projects)
    elif choice == "d":
        display_projects(projects)
    elif choice == "f":
        date_str = input("Show projects that start after date (dd/mm/yyyy): ")
        filter_projects_by_date(projects, date_str)
    elif choice == "a":
        add_project(projects)
    elif choice == "u":
        update_project(projects)
    elif choice == "q":
        save_choice = input("Would you like to save to projects.txt? ").strip().lower()
        if save_choice in ("yes", "y"):
            save_projects(FILENAME, projects)
        print("Thank you for using custom-built project management software.")
        return  # Exit the recursive loop
    else:
        print("Invalid option")

    run_menu(projects)

main()