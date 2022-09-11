#!/usr/bin/env python
"""
Performs basic cleaning on the data and save the results in Weights & Biases
"""
import argparse
import logging
import wandb
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact

    logger.info("Downloading data")
    artifact_local_path = run.use_artifact(args.input_artifact).file()
    data = pd.read_csv(artifact_local_path)

    logger.info("Dropping outliers")
    # Drop outliers
    idx = data['price'].between(args.min_price, args.max_price)
    data = data[idx].copy()

    logger.info("Type-casting datetime")
    # Convert last_review to datetime
    data['last_review'] = pd.to_datetime(data['last_review'])

    logger.info("Filtering data by longitude and latitude")
    idx = data['longitude'].between(-74.25, -73.50) & df['latitude'].between(40.5, 41.2)
    data = data[idx].copy()

    data.to_csv("clean_sample.csv", index=False)

    artifact = wandb.Artifact(
        args.output_artifact,
        type=args.output_type,
        description=args.output_description,
    )
    artifact.add_file("clean_sample.csv")

    logger.info("Logging artifact")
    run.log_artifact(artifact)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="This step cleans the data")


    parser.add_argument(
        "--input_artifact",
        type=str,
        help="Fully-qualified name for the input artifact",
        required=True
    )
    
    parser.add_argument(
        "--output_artifact",
        type=str,
        help="Name for the output artifact",
        required=True
    )
    
    parser.add_argument(
        "--output_type",
        type=str,
        help="Type for the artifact",
        required=False
    )

    parser.add_argument(
        "--output_description",
        type=str,
        help="Description for the output artifact",
        required=False,
    )

    parser.add_argument(
        "--min_price",
        type=float,
        help="Minimum price to keep in data",
        required=True
    )

    parser.add_argument(
        "--max_price",
        type=float,
        help="Maximum price to keep in data",
        required=True
    )


    args = parser.parse_args()

    go(args)
