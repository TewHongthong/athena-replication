# Masking report

GSCS map rows: 1020 (no comment: 21)
original unique GSCS items: 838 -> masked unique items: 837
rows whose comment changed: 702
labels masked per comment: {0: 297, 2: 4, 4: 698}

## reference / reference

before:
```
/* Function Objective: Compute the GPAX of one student
       Input parameters : f_point_total (float) weighted grade points, f_credit_total (float) registered credits
       Function description: Divide the weighted grade points by the registered credits, capped at the maximum GPAX
       Return Value : float GPAX value
       Created By : Programmer A
       Create Date: 2026-09-28
       Revised By:
       Revised Date:
    */
```
after:
```
/* Function Objective: Compute the GPAX of one student
       Input parameters : f_point_total (float) weighted grade points, f_credit_total (float) registered credits
       Function description: Divide the weighted grade points by the registered credits, capped at the maximum GPAX
       Return Value : float GPAX value
       Created By : [not inferable from code]
       Create Date: [not inferable from code]
       Revised By: [not inferable from code]
       Revised Date: [not inferable from code]
    */
```

## reference / reference

before:
```
/* Function Objective: Print one line of the grade report
   Input parameters : str_student_name (string) student name, f_gpax (float) GPAX value
   Function description: Shorten a long name to the maximum length, then print the name and the GPAX
   Return Value : void
   Created By : Programmer A
   Create Date: 2026-09-28
   Revised By:
   Revised Date:
*/
```
after:
```
/* Function Objective: Print one line of the grade report
   Input parameters : str_student_name (string) student name, f_gpax (float) GPAX value
   Function description: Shorten a long name to the maximum length, then print the name and the GPAX
   Return Value : void
   Created By : [not inferable from code]
   Create Date: [not inferable from code]
   Revised By: [not inferable from code]
   Revised Date: [not inferable from code]
*/
```

## reference / reference

before:
```
/* Function Objective: Store the name of a student
       Input parameters : str_new_name (string) the new student name
       Function description: Keep the new name, shortened to the maximum name size when it is too long
       Return Value : void
       Created By : Programmer A
       Create Date: 2026-09-28
       Revised By:
       Revised Date:
    */
```
after:
```
/* Function Objective: Store the name of a student
       Input parameters : str_new_name (string) the new student name
       Function description: Keep the new name, shortened to the maximum name size when it is too long
       Return Value : void
       Created By : [not inferable from code]
       Create Date: [not inferable from code]
       Revised By: [not inferable from code]
       Revised Date: [not inferable from code]
    */
```

## reference / reference

before:
```
/* Function Objective: Find the largest value in a list
   Input parameters : f_value_list (float array) the values, f_value_total (integer) number of values
   Function description: Start from the first value and keep the largest value seen while walking through the list
   Return Value : float largest value
   Created By : Programmer A
   Create Date: 2026-09-28
   Revised By:
   Revised Date:
*/
```
after:
```
/* Function Objective: Find the largest value in a list
   Input parameters : f_value_list (float array) the values, f_value_total (integer) number of values
   Function description: Start from the first value and keep the largest value seen while walking through the list
   Return Value : float largest value
   Created By : [not inferable from code]
   Create Date: [not inferable from code]
   Revised By: [not inferable from code]
   Revised Date: [not inferable from code]
*/
```
