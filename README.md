Setup environment and running this app in Docker environment

```docker build -t "simple-excel-app:v1" .```
```docker run --name  simple-excel-app:v1 ```

The output file to stout.

Input from stdin
The first line N specify the number of cells
The 2*N next line specify cell name and it values

Support basic math formula and cell references

Ex:
3
A1
5
A2
A1 5 * B1 +
B1
6

The formula written in the reverse polish notation (postfix) format