Usage
=====


Sharing a post
--------------

.. code-block:: python

  from linkedin_posts.posts import share_post

  r = share_post(
    "<HERE YOUR ACCESS TOKEN>",
    comment="publishing a post",
    author_type="organization",
    author_id="71513925",
  )

  # Do something with your response object r (http.client.HttpResponse)

  ...



Deleting a post
---------------

.. code-block:: python

  from linkedin_posts.posts import delete_post

  r = delete_post("<HERE YOUR ACCESS TOKEN>", "urn:li:share:7104319981684674560")

  # Do something with your response object r (http.client.HttpResponse)

  ...
