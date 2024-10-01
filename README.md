# Slackline placement

Slackline placement is a Python algorithm for choosing pairs of trees within a parc to install slacklines.

This greedy algorithme seeks to achieve the longest distance of slacklines as possible without any slacklines intersecting.

Other conditions include:

- A slackline must be attached to trees a and b.
- Only trees with a minimum diameter of 25cm can hold a slackline
- The maximum distance a slackline can be is 30m.
- The minimum distance a slackline must be is 5m.
- Stacklines can not intersect.
- Multiple slacklines can start from the same tree.
- Proximity between trees can be ignored to simplefie the problem.

## Usage

Use in terminal by replacing {parc name} with the corresponding file name.

```console
py .\SlacklinePlacement.py .\instances\instance_{parc name}.csv
```

Results will be produces in file name

```
resultat_instance_{parc name}.csv
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
