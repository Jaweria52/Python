from generateAbbreviations import generate_abbreviations
from scoreCounter import calculate_letter_score
from scoreCounter import calculate_abbreviation_score

created_abbr = []

def read_txt(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read lines, capitalize every letter, and write to a new file
            with open('javerianasereen.txt', 'w') as output_file:
                for line in file:
                    words = []
                    current_word = ''
                    for char in line.strip().upper():
                        if char.isalpha() or char.isspace():
                            current_word += char
                        elif char == '-':
                            current_word += ' '

                    if current_word:
                        words.extend(current_word.split())

                    if len(words) == 1:
                        without_first_letter = words[0][1:]
                        abbreviations = generate_abbreviations(without_first_letter,2)
                        
                        result = []
                        for abbr in abbreviations:
                            # Add the first letter of each word
                            full_word = current_word[0] + abbr
                            score = calculate_abbreviation_score(full_word, words[0])
                            if not created_abbr:
                                result.append((full_word, score))
                                created_abbr.append((full_word, score))
                            else:
                                is_record_exist = any(record[0] == full_word for record in created_abbr)
                                if not is_record_exist:
                                    result.append((full_word, score))
                                    created_abbr.append((full_word, score))


                        # created_abbr[full_word]=result
                       
                        result.sort(key=lambda x: x[1])  # Sort by score
                        formatted_result = ' '.join([f"{abbr} ({score})" for abbr, score in result])
                        # Write the original line and the formatted result to the output file
                        output_file.write(line.strip() + '\n')
                        if not result:
                            output_file.write("All possible Abbreviations have been generated" + '\n')
                        else:
                            output_file.write(result[0][0] + '\n')
                        # output_file.write(formatted_result + '\n')

                    elif len(words) == 2:
                        first_two_letters = words[0][0] +words[1][0]
                        abbreviations = []
                        for i in range(1, len(words[1])):
                            abbreviations.append(first_two_letters+words[1][i])
                        
                        result=[]
                        for abbr in abbreviations:
                            # print(abbr[len(abbr)-1],words[1])
                            score = calculate_letter_score(abbr[len(abbr)-1], False, True,words[1])
                            if not created_abbr:
                                result.append((abbr, score))
                                created_abbr.append((abbr, score))
                            else:
                                is_record_exist = any(record[0] == abbr for record in created_abbr)
                                if not is_record_exist:
                                    result.append((abbr, score))
                                    created_abbr.append((abbr, score))


                        pa=[]
                        
                        for i in range(1, len(words[0])):
                            score = calculate_letter_score(words[0][i], False, False,words[0])
                            pa.append((words[0][0]+words[0][i],score))
                        fl=[]
                        for j in range(len(pa)):
                            for i in range(len(words[1])):
                                score = calculate_letter_score(words[1][i], False, True,words[1])
                                try:
                                    if not created_abbr:
                                        fl.append((pa[j][0]+words[1][i],pa[j][1]+score))
                                        created_abbr.append((pa[j][0]+words[1][i],pa[j][1]+score))
                                    else:
                                        is_record_exist = any(record[0] == pa[j][0]+words[1][i] for record in created_abbr)
                                        if not is_record_exist:
                                            fl.append((pa[j][0]+words[1][i],pa[j][1]+score))
                                            created_abbr.append((pa[j][0]+words[1][i],pa[j][1]+score))
                                except IndexError as e:
                                    print("Error:", e)
                                    print("j:", j, "i:", i, "pa[j]:", pa[j])

                        #total= result+fl
                        result.sort(key=lambda x: x[1])  # Sort by score
                        #formatted_result = ' '.join([f"{abbr} ({score})" for abbr, score in total])
                        # Write the original line and the formatted result to the output file
                        output_file.write(line.strip() + '\n')
                        if not result:
                            output_file.write("All possible Abbreviations have been generated" + '\n')
                        else:
                            output_file.write(result[0][0] + '\n')

                    elif len(words) == 3:
                        first_two_letters = words[0][0] + words[1][0] + words[2][0]

                        if not created_abbr:
                            result.append((abbr, 0))
                            created_abbr.append((abbr, 0))
                        else:
                            is_record_exist = any(record[0] == abbr for record in created_abbr)
                            if not is_record_exist:
                                result.append((abbr,0))
                                created_abbr.append((abbr, 0))
                        created_abbr.append(first_two_letters)
                        output_file.write(line.strip() + '\n')
                        if not result:
                            output_file.write("All possible Abbreviations have been generated" + '\n')
                        else:
                         output_file.write(f"{first_two_letters}\n")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_path = input("Enter the name to the input file: ")
    read_txt(file_path)

if __name__ == "__main__":
    main()
