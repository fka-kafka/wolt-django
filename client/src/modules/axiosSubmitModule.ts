import axios from "axios";

const axiosCall = async (data: string) => {
  const responseData = await axios
    .post("/api/", data, {
      baseURL: "http://localhost:8000/",
      method: "post",
      headers: {
        "Content-Type": "application/json",
      },
      responseType: "json",
    })
    .then((res) => {
      console.log(res.data)
      return res.data.deliveryFee;
    });

  return responseData;
};

export default axiosCall;
