def my_name_is():
    print("My name is Rakib Hasan Topu")


def i_have_enrolled_course(course_name):
    print(f"I have enrolled in a course named {course_name}")


def i_have_learning(backend, frontend):
    return f"Learning {backend}, {frontend}"


course_and_learn=[
    {"course":"Python & Web", "frontend":"HTML, CSS, Bootstrap","backend":"Python"},
    {"course":"Java Spring Boot","frontend":"HTML, CSS, Hibernet","backend":"Java"},
    {"course":"C# & ASP.NET Core","frontend":"Entity Framework, Razor","backend":"C#"},
    {"course":"MERN Development","frontend":"Node, React, HTML","backend":"CSS"},
    {"course":"PHP & Laravel","frontend":"Blade, Eloquent","backend":"PHP"}
]
for item in course_and_learn:
    my_name_is()
    course_name=item["course"]
    i_have_enrolled_course(course_name)
    frontend=item["frontend"]
    backend=item["backend"]
    learning=i_have_learning(frontend,backend)
    print(learning)
    