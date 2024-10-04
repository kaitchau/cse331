import sys
import csv
import time
import hashlib
import itertools

# Brute-froce password cracker (MD5 hashing algo)
# PWs of length no longer than 4 chars

def read_pw_db_csv(file_path):
    pw_db_rows = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # append username, pw, salt
            pw_db_rows.append((row[0],row[1],row[2]))
    return pw_db_rows

def brute_force(data):
    start_time = time.time()
    output = []
    total = 0
    success_ct = 0
    alphanum = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    for user,pw,salt in data:
        cracked = False
        #do not consider pws of lengths longer than 4 chars
        for length in [1,2,3,4]:
            for cartesian in itertools.product(alphanum, repeat=length):
                guess = "".join(cartesian)
                hashed_guess = hashlib.md5(guess.encode()).hexdigest()

                if pw == hashed_guess:
                    cracked = True
                    success_ct+=1
                    output.append((user,guess))
                    break #break out of nested loop

            if cracked:
                break #break out of outer loop
        if not cracked:
            output.append((user,"FAILED"))
        total+=1
    end_time = time.time()
    total_time = end_time - start_time

    with open("task1.csv", "w") as file:
        writer = csv.writer(file)

        for row in output:
            writer.writerow(row)

        writer.writerow([f"TOTALTIME [{total_time:.2f} seconds]"])    
        success_rate = (success_ct/total)*100
        writer.writerow([f"SUCCESSRATE [{success_rate}%]"])
        
        

if __name__ == "__main__":
    pw_db_csv = sys.argv[1]
    pw_db = read_pw_db_csv(pw_db_csv)
    brute_force(pw_db)
