"""
Init Command Options related Datastructures for formatting.
"""
from typing import Dict, List

from samcli.cli.row_modifiers import RowDefinition

# The ordering of the option lists matter, they are the order in which options will be displayed.

APPLICATION_OPTIONS: List[str] = [
    "name",
    "architecture",
    "runtime",
    "dependency_manager",
    "location",
    "package_type",
    "base_image",
    "app_template",
    "output_dir",
]

# Can be used instead of the options in the first list
NON_INTERACTIVE_OPTIONS: List[str] = ["no_interactive", "no_input", "extra_context"]

CONFIGURATION_OPTION_NAMES: List[str] = ["config_env", "config_file"]

ADDITIONAL_OPTIONS: List[str] = [
    "tracing",
    "application_insights",
]

OTHER_OPTIONS: List[str] = ["debug"]

ALL_OPTIONS: List[str] = (
    APPLICATION_OPTIONS + NON_INTERACTIVE_OPTIONS + CONFIGURATION_OPTION_NAMES + ADDITIONAL_OPTIONS + OTHER_OPTIONS
)

OPTIONS_INFO: Dict[str, Dict] = {
    "Application Options": {
        "option_names": {opt: {"rank": idx} for idx, opt in enumerate(APPLICATION_OPTIONS)},
        "extras": [RowDefinition(name="")],
    },
    "Non Interactive Options": {
        "option_names": {opt: {"rank": idx} for idx, opt in enumerate(NON_INTERACTIVE_OPTIONS)}
    },
    "Configuration Options": {
        "option_names": {opt: {"rank": idx} for idx, opt in enumerate(CONFIGURATION_OPTION_NAMES)},
        "extras": [
            RowDefinition(name="Learn more about configuration files at:"),
            RowDefinition(
                name="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli"
                "-config.html. "
            ),
        ],
    },
    "Additional Options": {"option_names": {opt: {"rank": idx} for idx, opt in enumerate(ADDITIONAL_OPTIONS)}},
    "Other Options": {"option_names": {opt: {"rank": idx} for idx, opt in enumerate(OTHER_OPTIONS)}},
}
