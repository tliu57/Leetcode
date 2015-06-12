#!/usr/bin/python
class Solution:
	# @param {integer} A
	# @param {integer} B
	# @param {integer} C
	# @param {integer} D
	# @param {integer} E
	# @param {integer} F
	# @param {integer} G
	# @param {integer} H
	# @return {integer}
	def computeArea(self, A, B, C, D, E, F, G, H):
	        leftX = max(A, E)
		rightX = min(C, G)
		lowerY = max(F, B)
		upperY = min(D, H)
		overlap_area = 0
		if( leftX < rightX and lowerY < upperY ):
		       overlap_area = (rightX - leftX) * (upperY - lowerY)
		totalArea = ( C - A ) * ( D - B ) + ( G - E ) * ( H - F) - overlap_area
		return totalArea
