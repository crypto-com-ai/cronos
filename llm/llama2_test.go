package llm

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestInference(t *testing.T) {
	m, err := LoadModel("./stories15M.bin", "./tokenizer.bin")
	require.NoError(t, err)

	rsp, err := m.Inference("say hello", 1.0, 0, 256)
	require.NoError(t, err)
	require.NotEmpty(t, rsp)
}
