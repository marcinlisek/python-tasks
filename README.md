# FAQ

* never use the global variables inside the method - all things passed to method should be passed as an arguments.

* call the variables with full names instad of strange shortcuts (for example split_list instead of s_list)

* never call a method the same as a variable in this method.

* iterating through string we get single signs.

* for example instead of list_of_text_files call a variable text_files.

* what to do, if we havea method with multiple inputs and we want to return multiplbe values (SPOJ examples). Can we somehow add new variables? It probably would have to return a list or something.

* is it possible to have first filsted all the input data and then the output data?



* it is not posible to alter global variable with reasigning it inside the method. The case in the picture below shows this problem. Even though win_check method was run the global gameon didnt change.


![obraz](https://user-images.githubusercontent.com/94200668/143718471-5e9bc86c-11cb-40f0-8a9a-cca7dfc3cdf8.png)

* to run debug in pycharm, we ad a red dot marker next to line counter number and run debug
* it is important to preserve proper order of statements. Example is in the file "statements_order".
