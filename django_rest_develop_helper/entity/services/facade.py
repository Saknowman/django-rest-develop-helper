from columns.services.facade import make_column_code

def make_entity_code(entity):
    """
    Make code from entity for models.py

    Parameters
    ----------
    column : entity.models.entity.Entity

    Returns
    -------
    code : str
        ex:)
        from django.db import models

        class Book(models.Model):
            title = models.CharField(max_length=80, default='Title')
            author = models.ForeignKey(to='book.Author', related_name='books', on_delete=models.CASCADE)
    """

    import_lines =  "\n".join(['from django.db import models'])
    class_line_base = 'class {class_name}(models.Model):'
    columns_line_base = '\t{column}'

    class_line = class_line_base.format(class_name=entity.name)
    columns_line = "\n".join(
        columns_line_base.format(column=make_column_code(column.data))
        for column in entity.columns.all())
    result = "\n".join([
        import_lines,
        '',
        class_line,
        columns_line
    ])
    return result
