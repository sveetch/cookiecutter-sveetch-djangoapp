"""
================
API views mixins
================

"""


class ConditionalResumedSerializerMixin(object):
    """
    Overrides get_serializer_class to use a resumed Serializer in list.

    Set ``resumed_serializer_class`` attribute on your viewset to enable this behavior
    else the default serializer from ``serializer_class`` is always used.

    This won't work with classes which does not set attribute ``action`` like
    ``APIView``.

    The goal of this behavior is to have lighter payload on lists which does not need
    to return everything from an object.
    """
    def get_serializer_class(self):
        if self.action == "list":
            return self.resumed_serializer_class
        return super().get_serializer_class()
