.. _Django REST Framework: https://www.django-rest-framework.org/

.. _features_api_intro:

===
API
===

.. Note::
    This is an optional feature during creation of application project. It will only be
    available if you enabled it.

The application API is built with famous library `Django REST Framework`_ (also known
as DRF) and mounted on URL path ``api/``. You can reach this on your application URL
to browse API from your browser or an API client.

All API routes are DRF *viewset* using a different serializer depending you are
listing object or reading object details. This is implemented through viewset mixin
``ConditionalResumedSerializerMixin`` that use either a *resumed* serializer for object
list or the complete serializer in all other cases.

It is recommended to use a resumed serializer when listing object to avoid excessively
big payload in API response. However you will need to correctly think about what is
required to be in the list and what to only show in the detail.

If needed, you may disable this behavior by removing of
``ConditionalResumedSerializerMixin`` inheritage from your viewset and removing
viewset attribute ``resumed_serializer_class``.

The API does not implement or configure any specific security. The demonstration
sandbox just set the default option to allow edition for authenticated requests with
the right permission, anonymous requests will be able to read only.
