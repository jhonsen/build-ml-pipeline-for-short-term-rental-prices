# Predicting Short-Term Rental Prices in NYC
As a property management company, making estimations of property prices are essential to the success of the business. To this end, a machine learning model is employed to predict short-term rental prices in New York City based on rental prices of similar properties. The model is updated weekly with new data to reflect current estimate of the market.   

### Metrics and Model Registry
- [`Weights and Biases`: nyc_airbnb](https://wandb.ai/jhonsen/nyc_airbnb/overview?workspace=user-jhonsen)

### Repository structure
```
.
├── components           # pre-built utility modules 
│   ├── get_data         # data acquisition pipeline
│   ├── test_regression_model # model evaluation on test set
│   ├── train_val_test_split  # data segregation pipeline
│   └── wandb_utils      # utility
├── cookie-ml-flow-step  # cookie-cutter template
├── images               # tutorial images
├── config.yaml          # file used by Hydra configuration
├── MLproject            # main configuration file for MLFlow
├── README.md            # Project overview and instructions
├── src                  # source code for the project
│   ├── basic_cleaning   # data cleaning pipeline
│   ├── data_check       # data validation pipeline
│   ├── eda              # exploratory data analysis notebook
│   └── train_random_forest  # model training pipeline
└── main.py              # executable file to run project
└── environment.yml      # conda installation file

```

### Environment Setup
To train and run the model, ensure the environment is setup properly

```bash
> conda env create -f environment.yml
```



### Running the entire pipeline or individual steps
In order to run the entire pipeline when you are developing, execute:
```bash
>  mlflow run .
```
When developing, you can run individual piece of pipeline separately, e.g., to run only
the data acquisition step, run on the command line:

```bash
> mlflow run . -P steps=download
```
To run the ``download`` and the ``basic_cleaning`` steps only, execute:  
```bash
> mlflow run . -P steps=download,basic_cleaning
```

You can override any other parameter in the configuration file using the Hydra syntax, by
providing it as a ``hydra_options`` parameter. For example, say that we want to set the parameter
modeling -> random_forest -> n_estimators to 10 and etl->min_price to 50:

```bash
> mlflow run . \
  -P steps=download,basic_cleaning \
  -P hydra_options="modeling.random_forest.n_estimators=10 etl.min_price=50"
```


## License

[License](LICENSE.txt)
