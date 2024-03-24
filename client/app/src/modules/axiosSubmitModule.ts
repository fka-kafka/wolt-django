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
      if (res && res.data) {
        const result = JSON.parse(res.data);
        return result.delivery_fee;
      } else {
        throw new Error("Internal server error. Invalid response.", )
      }
    });

  return responseData;
};

export default axiosCall;
