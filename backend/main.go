package main

import (
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()

	r.Use(corsMiddleware())

	r.POST("/chat", handlerChat)

	r.Run(":8080")
}
