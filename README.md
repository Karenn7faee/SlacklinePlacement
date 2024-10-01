# Slackline placement

Slackline placement is a Python algorithm for choosing pairs of trees within a parc to install slacklines.

This greedy algorithme seeks to achieve the longest distance of slacklines as possible without any slacklines intersecting.

Other conditions include:

- A slackline must be attached to trees a and b.
- Only trees with a minimum diameter of 25cm can hold a slackline
- The maximum distance a slackline can be is 30m. distance(a,b) <= 30
- The minimum distance a slackline must be is 5m. distance(a,b) >= 5
- Stacklines can not intersect.
- Multiple slacklines can start from the same tree.
- Proximity between trees is ignored to simplify the problem.

## Usage

Use in terminal by replacing {parc name} with the corresponding file name.
The csv file instance\_{parc name}.csv must be in the same folder as SlacklinePlacement.py file to produce the correct result file.

```console
python SlacklinePlacement.py instance_{parc name}.csv
```

Outputs a csv file containing the pairs of tree indexes from within the instance\_{parc name}.csv in file named :

> resultat*instance*{parc name}.csv

More information can be found printed on the console

> num of trees in parc :
> num of possible slacklines :
> --- execution time : 0.00 seconds ---
> final distance covered :
> num of slacklines in solution :

## Contributing

Homework givin in Université de Montréal in the class "Introduction to algorithms".
All code comments and variables names are in french, only console prints were changed to english before adding to github .
