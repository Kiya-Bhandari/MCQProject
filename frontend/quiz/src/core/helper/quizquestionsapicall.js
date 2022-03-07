import { API } from "../../backend";
import { isAuthenticated } from "../../auth/helper";

export const questions = (quiz_id) => {
  return fetch(`${API}quizes/questions/${quiz_id}/`, {
    method: "GET",
  })
    .then((response) => {
      return response.json();
    })
    .catch((err) => console.log(err));
};

export const submitData = (quiz_id, data) => {
  const userId = isAuthenticated() && isAuthenticated().user.id;

  return fetch(`${API}results/save_quiz_view/${userId}/${quiz_id}/`, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => {
      return response.json();
    })
    .catch((err) => console.log(err));
};
