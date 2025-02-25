# 0x16. API advanced

## Learning Objectives

1. How to read API documentation to find the endpoints you are looking for
2. How to use an API with pagination
3. How to parse JSON results from an API
4. How to make a recursive API call
5. How to sort a dictionary by value

## How to read API documentation

1. The first step is to read the overview.
Most APi documentation has an overview section. This section generally covers basic information about the API, including what it does, how to connect to it and how to start using it.

### Learn the commonly used terms

#### ***Hypertext Transfer Protocol (Secure) (HTTP(S))***

This is a standardised protocol used to transfer data over a network. It is responsible for virtually all data exchanged through the internet.
HTTPS uses Secure Socket Layer (SSL) to encrypt requests, securing the connection.

#### ***HTTP Verbs***

HTTP request methods (verbs) are essentially the messenger between the client and the server.

Common HTTP verbs are:
**GET** - Used to retrieve data from a server.
**POST** - Used to send data, such as a username and a password on a form, to a server.
**PUT** - Used to replace all current representations of the target resource with the request payload. Essentially it is used to update an entire resource.
**DELETE** - Used to delete a specified resource.
**PATCH** - Used to apply partial modifications to a resource.

Context and Importance:

These HTTP verbs are fundamental to how web applications and APIs communicate. They define the intended action when a client (like a web browser) makes a request to a server.

It is very important to use the correct verb for the correct operation to maintain RESTful principles and ensure that the API behaves as expected. Using the wrong verb can lead to incorrect operations or unintended side effects.

#### ***Endpoint***

These are touch points allowing other applications to interact with other systems. Endpoints give you the location where that data can be retrieved from.

#### ***Request***

To retrive some data, a client sends an API request to the server, usually for information sy=uch as the endpoint of the data the client needs.

#### ***Response***

The requested data is known as a response and is commonly in JSON format. It could also be in XML, CSV, etc.

#### ***Header***

When an API request or an API response is sent, some metadata is sent along with it. The metadata usually contains information, such as the type of content included in the request body, the client's authentication token or credentials, as well as the cache policy defined by the server. This metadata is contained in an API header, and it offers additional details that facilitate the communication between the client and the server.

#### ***Response Status Codes***

These are standardized 3-digit numbers essential to signal success or failure.
Status codes not only signal that there is a failure or success, they also signal the type of failure/success that occured.
Common staus codes include:
*200* - OK
*404* - Not found
*401* - Unauthorized
*403* - Forbidden
*5XX* - Server side errors

## API Pagination

API Pagination is a technique that divides large datasets into smaller, manageable chunks (pages) for efficient retrieval, improving performance, reducing resource usage, and enhancing the user experience.

### Benefits of API Pagination

- **Improved performance**: Faster response times.
- **Reduced resource usage**: Less bandwidth, memory, and processing required.
- **Enhanced user experience**: Smoother navigation and quicker results.
- **Efficient data transfer**: Only necessary data is transferred.
- **Scalability and flexibility**: Better handling of large data volumes.
- **Error handling improvements**: Helps gracefully handle errors when retrieving data.

### Common Pagination Techniques

- **Offset and Limit**: Uses an offset (starting point) and limit (number of records) to paginate.
- **Cursor-Based**: A unique identifier (cursor) marks the position for pagination.
- **Page-Based**: A page parameter requests specific pages.
- **Time-Based**: Uses time ranges for temporal data pagination.
- **Keyset Pagination**: Sorts data based on a unique key for efficient pagination.

### Best Practices

- **Consistent Naming**: Use standard parameter names like `page`, `limit`.
- **Include Metadata**: Provide details such as total records, current page, next/previous page links.
- **Optimal Page Size**: Balance the amount of data per page with performance.
- **Sorting and Filtering**: Allow users to refine results.
- **Pagination Stability**: Ensure consistent data order between requests.
- **Edge Case Handling**: Gracefully handle errors like invalid page numbers.
- **Caching Strategies**: Implement caching for improved performance.

### Key Implementation Considerations

- Understand **data characteristics**.
- Consider **network latency** and **bandwidth**.
- Evaluate **performance impact**.
- Focus on **user experience** and usability.
- Provide **flexible pagination parameters**.
- Use **stable sorting mechanisms**.
- Ensure the use of **unique and immutable identifiers**.
- Apply **deterministic pagination techniques**.
- Provide **clear and informative error messages**.
- Implement **rate limiting and throttling**.
- Consider various caching methods:
  - Page-Level Caching
  - Result Set Caching
  - Time-Based Caching
  - Conditional Caching
  - Reverse Proxy Caching


## Transforming a JSON API Response Into a Python Dictionary

If you need to make an API request and convert its JSON response into a Python dictionary, here’s how you can do it using the `urllib` module and the `requests` library.

### Example: JSON Placeholder API

Consider the following API endpoint from the [JSONPlaceholder](https://jsonplaceholder.typicode.com) project, which returns fake JSON data:

`https://jsonplaceholder.typicode.com/todos/1`

#### Sample JSON Response

```json
{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
}
```

### Using `urllib` Module from the Standard Library

You can call this API with the `urllib` module and convert the resulting JSON into a Python dictionary as follows:

```python
import urllib.request
import json

url = "https://jsonplaceholder.typicode.com/todos/1"

with urllib.request.urlopen(url) as response:
    body_json = response.read()

body_dict = json.loads(body_json)
user_id = body_dict['userId']  # 1
```

### Explanation

- The `urllib.request.urlopen()` method performs the API call and returns an `HTTPResponse` object.
- The `read()` method is used to get the response body (`body_json`), which contains the API response as a JSON string.
- The `json.loads()` method parses that string into a Python dictionary.

## Using `requests` Library

Alternatively, you can achieve the same result using the `requests` library, which simplifies the process of working with APIs:

```python
import requests
import json

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

body_dict = response.json()
user_id = body_dict['userId']  # 1
```

### Explanation

- The `.json()` method of the `response` object automatically transforms the JSON data into the corresponding Python data structure.

### Conclusion

Now you know how to parse a JSON API response in Python using both the `urllib` module and the `requests` library. Both methods are effective, and the choice depends on your preference or specific use case.
