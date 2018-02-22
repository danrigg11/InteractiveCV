#Ask user for name
name = input("What is your'e name?: ")

#Ask user for age
age = input("How old are you?: ")

#Ask user what they enjoy
love = input("What do you enjoy?: ")

#skills
skills = """Digital artist 2D,3D, Other design and development software. Managing teams.

Software Experience: Windows XP, Microsoft Office, Python, Html, CSS, Adobe Photoshop, Autodesk Maya,
Autodesk Mudbox, Adobe After Effects, Final Cut Pro, Unreal Engine, Game Maker 2014/15,"""

#experience
experience = """Self employed (2016 – Present)
Roles:
Installations Manager – Conservatory roofing company.
Managing all installation teams; hotels, materials, customer care, accounts, data management.
Wix website & business forms developer.

Northwood Headquarters (MOD Base) (2015-2016)
Role: Onsite Transport.

VMC Studio (2015)
Role: Games Tester."""

#grades
grades = """Games Art & Design Degree at Norwich University of the Arts, graduating in 2014.
Games Design & Development at Uxbridge College – BTEC LEVEL Six-form Applied Art & Media studies at Barn-hill Community High."""

#contact details
contactdetails = """Email. dan_rigg11@hotmail.com,
Mobile. 07392826229."""

#create output text
string = """Hello {}
I hope you are having a greate day. Welcome to my interactive cv.
My name is Daniel Rigg and I am 26 years old, I cant believe youre only {}, looking good.

In my spare time I enjoy going to the gym and having chilled evenings with my friends and family,
I am also working on a couple projects, check them out on my portfolio.

I see you enjoy {}, remind me to ask you about this next time we meet.
Here is a list of my  skills & grades: {}

Education:{}

And {}, Lastly my work experiences:
{}

Thank you {} for youre time today please find my contact details below.
{}
"""
Output = string.format(name,age,love,skills,grades,name,experience,name,contactdetails)

#Print output on screen
print(Output)
Exit = input("Exit")

