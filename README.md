i have added this README in order to communicate with the reviewer: 

1. first specification that requires change

> 3rd Lambda: you’ve set a reasonable threshold (low 90s work best.) This will help verify if the model inference array has at least one value above the threshold value.
> You did a great job creating three lambda functions and deploying them. As part of your submission, you included the lambda function script files.
> However, the threshold you set is too high. You need to set a reasonable threshold between 55-80% ensuring that the model inference has at least one value above the threshold value.

i am not sure what to 'fix' as: 

- the filter threshold i used is 0.93/93%, which is not set by me to begin with, but rather set by the course designer, as the value came with the starter notebook
- this threshold value is a low 90%, which conforms to your comment 'low 90s work best'
- 9 out of 10 inferences i tried have come back with probabilities above this threshold, definitely satifies 'the model inference array has at least one value above the threshold value'

2. second specification that requires change

> Step Function does not ERROR AS EXPECTED when inference is below the confidence threshold
> 2x screenshot provided, showing passed and failed Step Function outcome.
> Perfect, you have composed the Step function and successfully executed it. I verified the JSON export that defines your Step Function.
> However, it is expected that you also have a screenshot of the Step Function that results in an ERROR AS EXPECTED when inference is below the confidence threshold.
> Changes Required
> Provide 2x screenshots, showing passed and failed Step Function outcome.
> Your screenshots for the successful and unsuccessful case should include more information, see the image below as an example:

- i will upload another screenshot for a successful example, which will show more info
  * 'screen_captures/step_function_successful_example_input.png'
  * 'screen_captures/step_function_successful_example_output.png'
- 'test/motorcycle_s_000446.png' is the test that did not meet the 0.93 threshold, which is the error example, i will add the respective screenshot
  * 'screen_captures/step_function_error_example_input.png'
  * 'screen_captures/step_function_error_example_output.png'
