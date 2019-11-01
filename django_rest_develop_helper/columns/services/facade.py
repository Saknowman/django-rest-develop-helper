
# ex
def make_column_code(column):
    """
    Make code from column for models.py

    Parameters
    ----------
    column : columns.models.column.Column

    Returns
    -------
    code : str
        ex:) title = models.CharField(max_length=80, default='Title')

    """

    base = "{name} = models.{field}({options})"
    result = base.format(
        name=column.name,
        field=column.type.value,
        options=', '.join(
            "{key}={value}".format(key=option.key, value=option.value)
            for option in column.options.all())
    )
    return result
