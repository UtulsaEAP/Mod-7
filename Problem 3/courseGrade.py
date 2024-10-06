def courseGrade():
    scores_file_name = None;
    report_file_name = "report.txt"

    # Initialize arrays for score data
    first_names = []
    last_names = []
    midterm1_scores = []
    midterm2_scores = []
    final_scores = []

    # Get the name of the student information file
    scores_file_name = input()

    # Read the scores
    with open(scores_file_name) as file:
        lines = file.readlines()

    # Distribute values from each line into separate lists
    for line in lines:
        fields = line.split()
        last_names.append(fields[0])
        first_names.append(fields[1])
        midterm1_scores.append(int(fields[2]))
        midterm2_scores.append(int(fields[3]))
        final_scores.append(int(fields[4]))

    # Open the report file for writing
    with open(report_file_name, "+w") as output_file:

        # Output the data and later grade for each student
        for n in range(len(first_names)):

            # Compute the letter grade
            average = (midterm1_scores[n]
                    + midterm2_scores[n]
                    + final_scores[n]) / 3
            if average >= 90:
                grade = "A"
            elif average >= 80:
                grade = "B"
            elif average >= 70:
                grade = "C"
            elif average >= 60:
                grade = "D"
            else:
                grade = "F"

            # Output the data and letter grade for each student
            print(f'{last_names[n]}\t{first_names[n]}\t'
                f'{midterm1_scores[n]}\t{midterm2_scores[n]}\t'
                f'{final_scores[n]}\t{grade}', file=output_file)

        # Write averages to file
        print(f'\nAverages: midterm1 {sum(midterm1_scores) / len(midterm1_scores):.2f}, '
            f'midterm2 {sum(midterm2_scores) / len(midterm2_scores):.2f}, '
            f'final {sum(final_scores) / len(final_scores):.2f}', 
            file=output_file)

    # TODO: Declare any necessary variables here. 
      
      
    # TODO: Read a file name from the user and read the tsv file here. 
   
   
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    return

if __name__ == "__main__":
    courseGrade()
    
    