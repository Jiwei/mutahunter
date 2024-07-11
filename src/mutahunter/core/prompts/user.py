USER_PROMPT = """
## Abstract Syntax Tree (AST) for Context
```ast
{{ast}}
```

## Response
The output must be in JSON format, wrapped in triple backticks (json...), and adhere to the following Pydantic definitions.
```
class SingleMutant(BaseModel):
    type: str = Field(description="The type of the mutation operator.(e.g., Off-by-One Error, Boundary Condition, Arithmetic, Block removal, Relational Operator, etc.)")
    description: str = Field(description="Description of the mutation.")
    context_before: str = Field(description="Line of code context before the mutation.")
    original_line: str = Field(description="The original line of code before mutation.")
    mutated_line: str = Field(description="The line of code after mutation, including a comment with the mutation description.")
    context_after: str = Field(description="Line of code context after the mutation.")

class Mutants(BaseModel):
    changes: List[Change] = Field(description="A list of changes representing the mutants.")
```

## Function Block to Mutate
Lines Covered: {{covered_lines}}. Only mutate lines that are covered by execution.
Note that we have manually added line numbers for each line of code. Do not include line numbers in your mutation. Make sure indentation is preserverd when generating mutants.
```{{language}}
{{function_block}}
```

Generate 1~{{maximum_num_of_mutants_per_function_block}} mutants for the function block provided to you. Ensure that the mutants are semantically different from the original code. Focus on critical areas such as error handling, boundary conditions, and logical branches.
"""