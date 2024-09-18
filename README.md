# Lecture 7- sep-18


## learned subjects

### Etra:
* colors in console- build-in:
  * colors of tables references: 
    * https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal/21786287#21786287 
    * https://gist.github.com/RabaDabaDoba/145049536f815903c79944599c6f952a
  * in the print() , you can style the output with text color, bold/bold intensity,underline ,background colors

  * examples:
   ```
   print("\033[1;92mBINGO\033[0m")  ## in BOLD with intensity in color green
   print(f"you guessed the number in \033[1;33m{tries}\033[0m tries") ## on the value of {tries} in yellow color
   ```
  ![img.png](img.png)