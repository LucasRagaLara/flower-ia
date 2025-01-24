document.getElementById('apiForm').addEventListener('submit', async function (event) {
  event.preventDefault();
  

  const length_sepal = document.getElementById('length_sepal').value;
  const length_petal = document.getElementById('length_petal').value;
  const width_sepal = document.getElementById('width_sepal').value;
  const width_petal = document.getElementById('width_petal').value;

    if (isNaN(length_sepal) || isNaN(length_petal)) {
      alert('Por favor, ingresa valores válidos para las medidas.');
      return;
    }
  try {
    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            length_sepal: parseFloat(length_sepal),
            length_petal: parseFloat(length_petal),
            width_sepal: parseFloat(width_sepal),
            width_petal: parseFloat(width_petal),
        }),
    });

    const result = await response.json();

    const resultDiv = document.getElementById('result');

    resultDiv.innerHTML = `Esta es tu flor: ${result.prediction}`;
    resultDiv.classList.add('animate-pulse');

    if (result.prediction === 'Setosa') {
      let contador = document.getElementById('contador');
      let count = parseInt(contador.innerHTML.split(': ')[1]);
      contador.innerHTML = `Setosa: ${count + 1}`;
    } else if (result.prediction === 'Versicolor') {
      let contador2 = document.getElementById('contador2');
      let count2 = parseInt(contador2.innerHTML.split(': ')[1]);
      contador2.innerHTML = `Versicolor: ${count2 + 1}`;
    } else if (result.prediction === 'Virginica') {
      let contador3 = document.getElementById('contador3');
      let count3 = parseInt(contador3.innerHTML.split(': ')[1]);
      contador3.innerHTML = `Virginica: ${count3 + 1}`;
    }
    
    setTimeout(() => {
      resultDiv.classList.remove('animate-pulse');
    }, 2000);

    document.getElementById('apiForm').reset();
  } catch (error) {
      alert('Ocurrió un error al procesar la solicitud. Intenta nuevamente.');
      console.error(error);
  }
});
