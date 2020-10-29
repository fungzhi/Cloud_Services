#!/usr/bin/env python3

from aws_cdk import core

from my_project.my_project_stack import MyProjectStack
from cdk.demo import CreateSNS


app = core.App()
MyProjectStack(app, "my-project")
CreateSNS(app, "cdk")

app.synth()
