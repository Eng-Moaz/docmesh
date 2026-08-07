package main

import (
	"bytes"
	"encoding/json"
	"io"
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
)


type ChatRequest struct{
	Question string `json:"question"`
	URL string `json:"url"`
}

type AIResponse struct{
	Answer  string   `json:"answer"`
	Sources []string `json:"sources"`
}

func handlerChat(c *gin.Context){
	var req ChatRequest

	if err := c.BindJSON(&req); err != nil{
		respondWithError(c, http.StatusBadRequest, err)
		return
	}

	log.Printf("Recieved from browser this question: %s \n", req.Question)
	log.Printf("Recieved from browser this url: %s \n", req.URL)

	body, _ := json.Marshal(req)	

	resp, err := http.Post(
		"http://localhost:8000/chat",
		"application/json",
		bytes.NewBuffer(body),
	)

	if err != nil{
		respondWithError(c, http.StatusInternalServerError, err)
		return
	}

	defer resp.Body.Close()

	data, _ := io.ReadAll(resp.Body)

	var ai AIResponse

	err = json.Unmarshal(data, &ai)

	if err != nil{
		respondWithError(c, http.StatusInternalServerError, err)
		return
	}

	log.Printf("Response from AI: %s", ai.Answer)
	c.JSON(http.StatusAccepted, ai)
}
