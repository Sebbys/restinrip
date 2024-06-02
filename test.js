const myHeaders = new Headers();
myHeaders.append("Content-Type", "application/x-www-form-urlencoded");

const formdata = new FormData();
formdata.append("age", "62");
formdata.append("anaemia", "0");
formdata.append("creatinine_phosphokinase", "231.0");
formdata.append("diabetes", "0");
formdata.append("ejection_fraction", "25");
formdata.append("high_blood_pressure", "1");
formdata.append("platelets", "253000.0");
formdata.append("serum_creatinine", "0.9");
formdata.append("serum_sodium", "140");
formdata.append("sex", "1");
formdata.append("smoking", "1");
formdata.append("time", "10");

const requestOptions = {
  method: "POST",
  body: formdata,
};

fetch("http://mahoraga.awscloudclub.id/predict", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.error(error));