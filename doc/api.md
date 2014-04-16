## POST /volumes/:name

**Resource URL**  
/api/1/volumes/:name

**Parameters**  
*bricks*(required)  
comma seperated paths

*replica* Numeric value, Replica count, default is 0
*stripe*  Numeric value, Stripe count, default is 0
*transport* String, Transport protocal(tcp|rdma|tcp,rdma) default is tcp
*force*   Use force while creating volume. boolean, true/false by default false

**Response Format**
Success:

    {
        "ok": true,
        "data": ""
    }

Failure:

    {
        "ok": false,
        "error": ""
    }


**Example Request**  
curl -XPOST http://localhost:8080/api/1/volumes/gvm -d bricks=



