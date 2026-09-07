#!/usr/bin/env python3

import aws_cdk as cdk
from stacks.daily_life_assistant import DailyLifeAssistantStack

app = cdk.App()

DailyLifeAssistantStack(
    app,
    "DailyLifeAssistantStack",
    env=cdk.Environment(
        account=None,
        region=None,
    ),
)

app.synth()