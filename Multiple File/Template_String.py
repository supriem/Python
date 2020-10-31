from string import Template
def main():
    # Usual string formatting with format()
    str1 = "I am learning {0} python from {1}.".format("advanced","linkedin learning")
    print(str1)
    
    # TODO: create a template with placeholders
    templ = Template("You're watching ${title} by ${By}. substituted by ${by}")
    # TODO: use the substitute  method with keyword arguments
    str2 = templ.substitute(title = "Advanced Python", By = "Linkedin", by = "kwargs")
    print(str2)
    
    # TODO: use substitute methd with dictionary
    data = { 'By':'Linkedin',
             'title':'Advanced Python',
             "by" : "dictionary"
             }
    str3 = templ.substitute(data)
    print(str3)
    
if __name__ == "__main__":
    main()