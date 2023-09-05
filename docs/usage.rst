Usage
=====


Sharing a post
--------------

.. code-block:: python

  from linkedin_posts.posts import share_post

  response = share_post(
    "<HERE YOUR ACCESS TOKEN>",
    comment="publishing a post",
    author_type="organization",
    author_id="71513925",
  )

  # Do something with your response object r (http.client.HttpResponse)
  # Interesting parameters to check:
  # response.getheader("x-restli-id") will return the Linkedin Post ID
  # response.code will return 201 if request proccessed correctly
  ...



Deleting a post
---------------

.. code-block:: python

  from linkedin_posts.posts import delete_post

  response = delete_post("<HERE YOUR ACCESS TOKEN>", "urn:li:share:7104319981684674560")

  # response.code will return 204 if request proccessed correctly

