package main

import (
	"github.com/gin-gonic/gin"
)

func respondWithError(c *gin.Context, statusCode int, err error){
	c.JSON(
		statusCode,
		gin.H{
			"error": err.Error(),
		},
	)
}
