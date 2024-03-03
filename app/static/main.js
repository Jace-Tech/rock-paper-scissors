const buttons = document.querySelectorAll("button")
const resultScreen = document.querySelector("#result")
const vsArea = document.querySelector("#vs")
const choiceMap = {
  s: "✂️",
  r: "🪨",
  p: "📄"
}


const updateScreen = (result) => {
  const { message, success, data } = result
  if(!success) throw Error(message || "Something went wrong")
  const { won, user, computer } = data
  const isTie = message.toLowerCase().includes("tie")

  // DISPLAY RESULT SCREEN
  resultScreen.className = ""
  resultScreen.innerHTML = `${message} ${isTie ? "" : won ? "🎉🏆🌟" : "😫😢😭"}`
  if(!isTie) {
    if(won) resultScreen.classList.add("success")
    else resultScreen.classList.add("danger")
    
  }
  resultScreen.classList.add("show")


  // UPDATE VS AREA
  const userScreen = vsArea.querySelector("#user")
  const computerScreen = vsArea.querySelector("#computer")
  vsArea.className = ""
  userScreen.querySelector("span").innerHTML = choiceMap[user]
  computerScreen.querySelector("span").innerHTML = choiceMap[computer]
  vsArea.classList.add("show")
}


const handleCheck = async (event) => {
  try {
    const choice = event.target.name
    const request = await fetch("/check", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ choice })
    })
    const response = await request.json()
    updateScreen(response)
  } catch (error) {
    console.log("ERROR:", error.message)
  }
}


buttons.forEach(btn => {
  btn.addEventListener("click", handleCheck)
})