function addSkill() {
    let name = document.getElementById("name").value;
    let skill = document.getElementById("skill").value;

    document.getElementById("studentName").innerText = name + "'s Skills";

    let li = document.createElement("li");
    li.innerText = skill;

    document.getElementById("skillList").appendChild(li);
}