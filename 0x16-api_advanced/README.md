# 0x16. API advanced

## Learning Objectives

1. How to read API documentation to find the endpoints you are looking for
2. How to use an API with pagination
3. How to parse JSON results from an API
4. How to make a recursive API call
5. How to sort a dictionary by value

### How to read API documentation

1. The first step is to read the overview.
Most APi documentation has an overview section. This section generally covers basic information about the API, including what it does, how to connect to it and how to start using it.

2. Learn the commonly used terms.
**Hypertext Transfer Protocol (Secure) (HTTP(S))**
This is a standardised protocol used to transfer data over a network. It is responsible for virtually all data exchanged through the internet.
HTTPS uses Secure Socket Layer (SSL) to encrypt requests, securing the connection.

**HTTP Verbs**
HTTP request methods (verbs) are essentially the messenger between the client and the server.
Common HTTP verbs are:
*GET* - Used to retreive data from a server
*POST* - Used to send data, such as a username and a password on a form, to a server.
*PUT* -
*DELETE* -
*PATCH* -

**Endpoint**
These are touch points allowing other applications to interact with other systems. Endpoints give you the location where that data can be retrieved from.

**Request**
To retrive some data, a client sends an API request to the server, usually for information sy=uch as the endpoint of the data the client needs.

**Response**
The requested data is known as a response and is commonly in JSON format. It could also be in XML, CSV, etc.

**Header**
When an API request or an API response is sent, some metadata is sent along with it. The metadata usually contains information, such as the type of content included in the request body, the client's authentication token or credentials, as well as the cache policy defined by the server. This metadata is contained in an API header, and it offers additional details that facilitate the communication between the client and the server.

**Response Status Codes**
These are standardized 3-digit numbers essential to signal success or failure.
Status codes not only signal that there is a failure or success, they also signal the type of failure/success that occured.
Common staus codes include:
*200* - OK
*404* - Not found
*401* - Unauthorized
*403* - Forbidden
*5XX* - Server side errors

### How to use an API with pagination
