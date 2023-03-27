# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1903067
# Date:18/04/2022

progress = []
progress_module_trailer = []
module_retriever = []
exclude = []

list_1 = [progress, progress_module_trailer, module_retriever, exclude]


def calc_outcome(): 
    done = False
    while not done:
        try:
            pass_num = int(input("\nPlease enter your credits at pass: "))

            if pass_num % 20 == 0 and pass_num < 121:    
                print("")

            else: 
                print("Out of range\n")
                break
        
            defer_num = input("Please enter your credits at defer: ")

            defer_num = int(defer_num)
            if defer_num % 20 == 0 and defer_num < 121:    
                print("")
            
            else: 
                print("Out of range\n")
                break


            fail_num = input("Please enter your credits at fail: ")

            fail_num = int(fail_num)
            if fail_num % 20 == 0 and fail_num < 121:    
                print("")

            else: 
                print("Out of range\n")
                break

        except ValueError:
            print("Integer required\n")
            break
            
        #determining the progression outcome applicable to the inputs entered
        total = pass_num + defer_num + fail_num
        if total == 120:
            if pass_num == 120 :
                print("Progress\n")
                progress.append(total) 
            
            elif pass_num == 100 :
                print("Progress (module trailer)\n") 
                progress_module_trailer.append(total) 
        
            elif fail_num >= 80 :
                print("Exclude\n")
                exclude.append(total) 
        
            else: 
                print("Module retriever\n")
                module_retriever.append(total)

        else:
            print("Total incorrect\n")
            break

        if total == 120:
            done = True


#function to display horizontal histogram
def h_histogram():        
    print("-" * 100)
    print("Progress", len(progress), " :", "*" * len(progress))
    print("Trailer", len(progress_module_trailer), "  :", "*" * len(progress_module_trailer))
    print("Retriever", len(module_retriever), ":", "*" * len(module_retriever))
    print("Excluded", len(exclude), " :", "*" * len(exclude))

    count_outcomes = len(progress) + len(progress_module_trailer) + len(module_retriever) + len(exclude)
    print()
    print(count_outcomes, "outcomes in total.")
    print("-" * 100)


#function to display vertical histogram 
def v_histogram():        
    for i in list_1:
        if len(i) > 0:
            print("   ", "*", "     ", end="  ")
            i.pop()
        else:
            print("   ", " ", "     ", end="  ")
    

def main():
  
    option  = ''
    option = input("Progression Outcome Program\nEnter 'y' to start or 'q' to quit to view results: ")
    while option == 'y':
        calc_outcome()
        option = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit to view results: ")
        
    while option == 'q':
        h_histogram()
        count_outcomes = len(progress) + len(progress_module_trailer) + len(module_retriever) + len(exclude)

        #prints vertical histogram
        print("Progress", len(progress), "|", "Trailer", len(progress_module_trailer), "|", "Retriever", len(module_retriever), "|", "Exclude", len(exclude))

        for x in range(count_outcomes):               
            v_histogram()
            print()
        print(count_outcomes, "outcomes in total.")
        print("-" * 100)
        break

main()
