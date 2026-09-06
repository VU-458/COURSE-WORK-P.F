# Smart Study Planner

FILE = "study_log.txt"


def classify_session(duration):
    if duration < 30:
        return "Short"
    elif duration <= 90:
        return "Medium"
    else:
        return "Long"


def add_session(sessions):
    subject = input("Subject: ")
    topic = input("Topic: ")
    date = input("Date/Day: ")

    while True:
        try:
            duration = float(input("Duration in minutes: "))
            if duration > 0:
                break
            print("Enter a positive number.")
        except ValueError:
            print("Enter a valid number.")

    sessions.append({
        "subject": subject,
        "topic": topic,
        "date": date,
        "duration": duration
    })

    print("Session added.")


def view_sessions(sessions):
    if not sessions:
        print("No sessions recorded.")
        return

    print("\nSubject\t\tTopic\t\tDate\t\tMinutes\tType")

    for s in sessions:
        print(
            f"{s['subject']}\t\t{s['topic']}\t\t"
            f"{s['date']}\t\t{s['duration']}\t"
            f"{classify_session(s['duration'])}"
        )


def search_by_subject(sessions):
    subject = input("Enter subject: ")
    total = 0
    found = False

    for s in sessions:
        if s["subject"].lower() == subject.lower():
            print(
                s["subject"], "-", s["topic"],
                "-", s["duration"], "minutes",
                "-", classify_session(s["duration"])
            )
            total += s["duration"]
            found = True

    if found:
        print("Total time:", total, "minutes")
    else:
        print("No sessions found for", subject)


def study_statistics(sessions):
    if not sessions:
        print("No sessions recorded.")
        return

    total = sum(s["duration"] for s in sessions)
    print("Total hours:", round(total / 60, 2))

    subjects = {}

    for s in sessions:
        subjects[s["subject"]] = subjects.get(
            s["subject"], 0
        ) + s["duration"]

    print("\nHours per subject:")
    for subject, minutes in subjects.items():
        print(subject, ":", round(minutes / 60, 2))

    weakest = min(subjects, key=subjects.get)
    longest = max(sessions, key=lambda s: s["duration"])

    print("Least study time:", weakest)
    print(
        "Longest session:", longest["subject"],
        "-", longest["duration"], "minutes"
    )


def save_sessions(sessions):
    with open(FILE, "w") as file:
        for s in sessions:
            file.write(
                f"{s['subject']}|{s['topic']}|"
                f"{s['date']}|{s['duration']}\n"
            )


def load_sessions():
    sessions = []

    try:
        with open(FILE, "r") as file:
            for line in file:
                subject, topic, date, duration = line.strip().split("|")

                sessions.append({
                    "subject": subject,
                    "topic": topic,
                    "date": date,
                    "duration": float(duration)
                })

    except FileNotFoundError:
        pass

    return sessions


def main():
    sessions = load_sessions()

    while True:
        print("\n1. Add session")
        print("2. View sessions")
        print("3. Search by subject")
        print("4. View statistics")
        print("5. Save and exit")

        choice = input("Choose: ")

        if choice == "1":
            add_session(sessions)
        elif choice == "2":
            view_sessions(sessions)
        elif choice == "3":
            search_by_subject(sessions)
        elif choice == "4":
            study_statistics(sessions)
        elif choice == "5":
            save_sessions(sessions)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

