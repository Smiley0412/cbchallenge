import axios from "axios";

const endPoint = process.env.VUE_APP_SERVER_API_ENDPOINT
const headers = {
  Authorization: `Token ${localStorage.getItem("cb_token")}`
}

/**
 * Function login
 * @param {*} params { username : admin, password : password }
 * @returns { message: '', status: 200 }
 */
export async function login(params) {
  try {
    const authorization = await axios.post(
      `${endPoint}/auth/login/`, params
    );
    localStorage.setItem("cb_user_id", authorization.data.user.id);
    localStorage.setItem("cb_token", authorization.data.token);
    return {
      message: `Welcome ${params.username}!, Please Enjoy.`,
      status: 200
    };
  } catch (error) {
    return getErrorCode(error);
  }
}

/**
 * Function signup
 * @param {*} params { username : admin, email: a@a.com, password : password }
 * @returns { message: '', status: 200 }
 */
export async function signup(params) {
  try {
    await axios.post(
      `${endPoint}/auth/signup/`, params
    );
    return {
      message: `Welcome ${params.username}!, Please login.`,
      status: 200
    };
  } catch (error) {
    return getErrorCode(error);
  }
}

/**
 * Function getMessagesList
 * @param {*} params { user : 1, sent : true }
 * @returns array message[]
 * 
 * If sent is set, retrieve all sent messages,
 * else retrieve all receipt messages.
 */
export async function getMessagesList(params) {
  try {
    const result = await axios.get(
      `${endPoint}/messages/`, { params: params, headers: headers }
    );
    return result.data;
  } catch (error) {
    console.log(error);
    return [];
  }
}

/**
 * Function getSingleMessage
 * @param {*} params { id : 1 }
 * @returns object 
 */
export async function getSingleMessage(id) {
  try {
    const result = await axios.get(
      `${endPoint}/messages/${id}`, { headers: headers }
    );
    console.log(result);
    return result;
  } catch (error) {
    console.log(error);
    return getErrorCode(error);
  }
}

/**
 * Function removeMessage
 * @param {*} params { id : 1 }
 * @returns object 
 */
export async function removeMessage(id) {
  try {
    await axios.delete(
      `${endPoint}/messages/${id}`, { headers: headers }
    );
    return {
      message: "Successfully Removed!",
      status: 200
    };
  } catch (error) {
    return getErrorCode(error);
  }
}

/**
 * Function getAllUsers
 * @returns array user[]
 * 
 * Retrieve all users signed it this app.
 */
export async function getAllUsers() {
  try {
    const result = await axios.post(
      `${endPoint}/users/`, {}, { headers: headers }
    );
    return result.data;
  } catch (error) {
    console.log(error);
    return [];
  }
}


export async function sendNewMessage(params) {
  try {
    await axios.post(
      `${endPoint}/messages/`, params, { headers: headers }
    );
    return {
      message: "Successfully Sent!",
      status: 200
    };
  } catch (error) {
    console.log(error);
    return getErrorCode(error);
  }
}

/**
 * Function getErrorCode
 * @param {*} error 
 * @returns { message: error_reason, status: error_status }
 */
function getErrorCode(error) {
  if (error.response.status === 404) {
    return {
      message: [error?.response?.data?.error],
      status: 404
    }
  } else if (error.response.status === 400) {
    return {
      message: error?.response?.data?.error,
      status: 400
    }
  } else {
    return {
      message: error?.message,
      status: error.response.status
    }
  }
}