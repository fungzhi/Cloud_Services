from aws_cdk.core import App, Construct
from aws_cdk import (
    aws_sns as sns,
    core
    )
    
class CreateSNS(core.Stack):
     # Create an Amazon SNS Topic: "Insurance-Quote-Reqests" //
    def __init__(self, app: core.App, id: str, **kwargs) -> None:
        super().__init__(app, id)
       
        MyTopic = sns.Topic(
            self, "ANS-Insurance-Quote-Reqests", 
            topic_name="ANS-Insurance-Quote-Reqests"
            )
           