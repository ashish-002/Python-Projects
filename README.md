# Python-Projects

# BMI Calculator

This is a simple BMI (Body Mass Index) calculator written in Python. It calculates the BMI based on the provided height and weight values and determines whether the person is overweight or not.

## Usage

1. Set the `name`, `height_m`, and `weight_kg` variables in the code with the appropriate values.
2. Run the script.
3. The calculated BMI will be displayed, along with a message indicating whether the person is overweight or not.

## Example

```python
name = "Atom"
height_m = 2
weight_kg = 110
bmi = weight_kg / (height_m ** height_m)
print("BMI:")
print(bmi)
if bmi < 25:
    print(name)
    print("is not overweight")
else:
    print(name)
    print("is overweight")
